import type { LinksFunction, LoaderFunction } from "@remix-run/node";
import { json } from "@remix-run/node";
import {
  useLoaderData,
  useCatch,
  Form,
  Link,
} from "@remix-run/react";
import type { Movie } from "@prisma/client";

import { db } from "~/utils/db.server";

import { MoviePosterItem } from "~/components/movie";
type LoaderData = { randomMovie: (Movie & {
    genres: string[];
})[]};

export const loader: LoaderFunction = async () => {
  const randomMovie = await db.movie.findMany({
    include: { 
      genres: { 
        include: { 
          genre: {
            select: {
              name: true,
            }
          },
        }
      },
    }
  });
  if (!randomMovie || randomMovie.length === 0) {
    throw new Response("No movie to show", {
      status: 404,
    });
  }
  const data: LoaderData = {
    randomMovie: randomMovie.map(movie => {
      const genres = movie.genres.map(genre => genre.genre.name)
      return { 
        ...movie,
        genres: genres,
      }
    })
  }
  return json(data);
};

export default function MoviesIndexRoute() {
  const data = useLoaderData<LoaderData>();

  return (
    <div className="relative overflow-scroll h-full">
      <div className="h-full overflow-auto grid gap-4 grid-cols-5">
        {data.randomMovie.map(movie => (
          <Link key={movie.id} to={movie.title}>
            <MoviePosterItem movie={movie} />
          </Link>
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