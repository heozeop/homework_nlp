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
  title: "Movie I want",
  description:
    "Movie finder! Find movie that you want to feel",
});

export default function Index() {
  return (
    <div className="container">
      <div className="content">
        <h1>
          I want to find <span>Movies!</span>
        </h1>
        <h2>
          Which like ...
        </h2>
        <nav>
          <ul>
            <li>
              <Link to="jokes">Read Jokes</Link>
            </li>
          </ul>
        </nav>
      </div>
    </div>
  );
}