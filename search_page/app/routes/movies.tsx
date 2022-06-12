import type {
  ActionFunction,
  LinksFunction,
  LoaderFunction,
} from "@remix-run/node";
import { json } from "@remix-run/node";
import {
  Form,
  Link,
  Outlet,
  useLoaderData,
  useSearchParams,
  useTransition,
} from "@remix-run/react";

import { db } from "~/utils/db.server";
import { getUser } from "~/utils/session.server";
import stylesUrl from "~/styles/movies.css";
import { useEffect, useState } from "react";

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
  const [searchParams] = useSearchParams()
  const text = searchParams.get("text");

  const [textString, setTextString] = useState(text ?? '')

  useEffect(() => {
    if (text && !textString) {
      setTextString(text)
    }
  }, [text, textString])

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
              <span className="logo-medium">IMSDB searcher</span>
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
        <div className="movies-search">
          <div className="container">
            <Form method="get">
              <input
                value={textString}
                onChange={(e) => {
                  setTextString(e.target.value)
                }}
                className="h-full"
                name="text"
                type="search"
                placeholder="Search the content you want to see or emotions you want to feel"
              />
              <button type="submit" className="button">
                Search
              </button>
            </Form>
          </div>
        </div>
      </header>
      <main className="movies-main">
          <div className="container">
          <div className="movies-outlet">
            <Outlet />
          </div>
        </div>
      </main>
    </div>
  );
}