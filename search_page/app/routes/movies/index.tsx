import type { LoaderFunction } from "@remix-run/node";
import { json } from "@remix-run/node";
import {
  useLoaderData,
  useCatch,
  useTransition,
} from "@remix-run/react";
import type { Movie } from "@prisma/client";

import { db } from "~/utils/db.server";

import { MoviePosterItem } from "~/components/movie";
import { searchApi } from "~/apis/search";

import ClimbingBoxLoader from 'react-spinners/ClimbingBoxLoader';

type LoaderData = { randomMovie: (Movie & {
    genres: string[];
})[]};

export const loader: LoaderFunction = async ({ request }) => {
  const url = new URL(request.url);
  const text = url.searchParams.get("text");
  const count = parseInt(url.searchParams.get('count') ?? '10', 10);
  const randomRowNumber = Math.floor(Math.random() * count); 
  const baseOptions = { 
    take: count,
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
  }

  let randomMovie = []
  if (!text || text.length < 1) {
    randomMovie = await db.movie.findMany({
      skip: randomRowNumber,
      ...baseOptions
    });
  } else {
    const searchResult = await searchApi({ text });
    randomMovie = await db.movie.findMany({
      where: {
        OR: searchResult.movies.map(title => ({
          title: title.replaceAll('-',' '),
        }))
      },
      ...baseOptions
    });
  }


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
  const trainsition = useTransition()


  return (
    <div className="relative overflow-scroll h-full">
      {trainsition.state === 'submitting' ?
          <div className="flex center w-full h-full">
            <ClimbingBoxLoader color={"#ededed"} />
            <p>로딩 중~~</p>
          </div>
        : <div className="h-full overflow-auto grid gap-4 grid-cols-5">
            {data.randomMovie.map(movie => (
              <a key={movie.id} href={`https://imsdb.com/scripts/${movie.title.replaceAll(' ','-')}.html`} target="_blank" rel="noreferrer">
                <MoviePosterItem movie={movie} />
              </a>
            ))}
          </div>
        }
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