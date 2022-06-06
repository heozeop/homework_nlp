import type {
  LinksFunction,
  MetaFunction,
} from "@remix-run/node";
import { Link } from "@remix-run/react";

import stylesUrl from "~/styles/index.css";

export const links: LinksFunction = () => {
  return [{ rel: "stylesheet", href: stylesUrl }];
};

export const meta: MetaFunction = () => ({
  title: "Movie Scripts I want",
  description:
    "Movie Script finder! Find movie that you want to feel",
});

export default function Index() {
  return (
    <div className="container">
      <div className="content">
        <h1>
          I want to find <span>Movie Scripts!</span>
        </h1>
        <nav>
          <ul>
            <li>
              <Link to="movies">find movie scripts</Link>
            </li>
          </ul>
        </nav>
      </div>
    </div>
  );
}