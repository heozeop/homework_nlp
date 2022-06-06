import type { LoaderFunction } from "@remix-run/node";
import { json } from "@remix-run/node";
import {
  useLoaderData,
  Link,
  useCatch,
} from "@remix-run/react";
import type { Movie } from "@prisma/client";

import { db } from "~/utils/db.server";

type LoaderData = { randomMovie: Movie};

export const loader: LoaderFunction = async () => {
  const count = await db.movie.count();
  const randomRowNumber = Math.floor(Math.random() * count);
  const [randomMovie] = await db.movie.findMany({
    take: 1,
    skip: randomRowNumber,
  });
  if (!randomMovie) {
    throw new Response("No random joke found", {
      status: 404,
    });
  }
  const data: LoaderData = { randomMovie };
  return json(data);
};

export default function JokesIndexRoute() {
  const data = useLoaderData<LoaderData>();

  return (
    <div>
      <p>{data.randomMovie.title}</p>
      <Link prefetch="intent" to={data.randomMovie.id}>
        "{data.randomMovie.title}" Permalink
      </Link>
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