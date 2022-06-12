import type { LinksFunction, LoaderFunction } from "@remix-run/node";
import { json } from "@remix-run/node";
import {
  useLoaderData,
  useCatch,
  Form,
} from "@remix-run/react";
import type { Movie } from "@prisma/client";

import { db } from "~/utils/db.server";

import stylesUrl from "~/styles/movies-index.css";
import { MovieDisplay } from "~/components/movie";

export const links: LinksFunction = () => {
  return [{ rel: "stylesheet", href: stylesUrl }];
};

type LoaderData = { randomMovie: Movie[]};

export const loader: LoaderFunction = async () => {
  const randomMovie = await db.movie.findMany();
  if (!randomMovie || randomMovie.length === 0) {
    throw new Response("No movie to show", {
      status: 404,
    });
  }
  const data: LoaderData = { randomMovie };
  return json(data);
};

export default function MoviesIndexRoute() {
  const data = useLoaderData<LoaderData>();

  return (
    <div className="relative overflow-scroll h-full">
      <div className="movies-posters">
        {data.randomMovie.map(movie => (
          <MovieDisplay movie={movie} />
        ))}
      </div>
    </div>
  );
}

export function CatchBoundary() {
  const caught = useCatch();

  if (caught.status === 404) {
    return (
      <div className="error-container">
        There are no jokes to display.
      </div>
    );
  }
  throw new Error(
    `Unexpected caught response with status: ${caught.status}`
  );
}

export function ErrorBoundary() {
  return (
    <div className="error-container">
      I did a whoopsies.
    </div>
  );
}