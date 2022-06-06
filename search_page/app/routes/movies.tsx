import type {
  LinksFunction,
  LoaderFunction,
} from "@remix-run/node";
import { json } from "@remix-run/node";
import {
  Form,
  Link,
  Outlet,
  useLoaderData,
} from "@remix-run/react";

import { db } from "~/utils/db.server";
import { getUser } from "~/utils/session.server";
import stylesUrl from "~/styles/jokes.css";

export const links: LinksFunction = () => {
  return [{ rel: "stylesheet", href: stylesUrl }];
};

type LoaderData = {
  user: Awaited<ReturnType<typeof getUser>>;
  genreList: Array<{ id: string, name: string }>;
};

export const loader: LoaderFunction = async ({
  request,
}) => {
  const genreListItems = await db.genre.findMany({
    select: {id: true, name: true}
  });

  const user = await getUser(request);

  const data: LoaderData = {
    genreList: genreListItems,
    user,
  };
  return json(data);
};

export default function MoviesRoute() {
  const data = useLoaderData<LoaderData>();

  return (
    <div className="movies-layout">
      <header className="movies-header">
        <div className="container">
          <h1 className="home-link">
            <Link
              to="/"
              title="Movies"
              aria-label="Movies"
            >
              <span className="logo-medium">M🤪VIES</span>
            </Link>
          </h1>
          {data.user ? (
            <div className="user-info">
              <span>{`Hi ${data.user.username}`}</span>
              <Form action="/logout" method="post">
                <button type="submit" className="button">
                  Logout
                </button>
              </Form>
            </div>
          ) : (
            <Link to="/login">Login</Link>
          )}
        </div>
      </header>
      <main className="jokes-main">
        <div className="container">
          <div className="jokes-list">
            <Link to=".">Get a random Movie</Link>
            <p>Genres</p>
            <ul>
              {data.genreList.map((movie) => (
                <li key={movie.id}>
                  <Link to={movie.id}>{movie.name}</Link>
                </li>
              ))}
            </ul>
            {/* <Link to="new" className="button">
              Add your own
            </Link> */}
          </div>
          <div className="jokes-outlet">
            <Outlet />
          </div>
        </div>
      </main>
    </div>
  );
}