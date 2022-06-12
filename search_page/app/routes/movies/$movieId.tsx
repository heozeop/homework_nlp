import type {
  LoaderFunction,
  MetaFunction,
} from "@remix-run/node";
import { json} from "@remix-run/node";
import {
  useLoaderData,
  useCatch,
  useParams,
} from "@remix-run/react";
import type { Movie } from "@prisma/client";

import { db } from "~/utils/db.server";
import { MoviePosterItem } from "~/components/movie";
export const meta: MetaFunction = ({
  data,
}: {
  data: LoaderData | undefined;
}) => {
  if (!data) {
    return {
      title: "No matching",
      description: "No movie found",
    };
  }
  return {
    title: `"${data.movie.title}" Script`,
    description: `Enjoy the "${data.movie.title}" script and much more`,
  };
};

type LoaderData = { movie: Movie; };

export const loader: LoaderFunction = async ({
  params,
}) => {
  const movie = await db.movie.findUnique({
    where: { id: params.movieId},
  });
  if (!movie) {
    throw new Response("What a joke! Not found.", {
      status: 404,
    });
  }
  const data: LoaderData = {
    movie,
  };
  return json(data);
};


export default function JokeRoute() {
  const data = useLoaderData<LoaderData>();

  return (
    <MoviePosterItem movie={data.movie} />
  );
}

export function CatchBoundary() {
  const caught = useCatch();
  const params = useParams();
  switch (caught.status) {
    case 400: {
      return (
        <div className="error-container">
          What you're trying to do is not allowed.
        </div>
      );
    }
    case 404: {
      return (
        <div className="error-container">
          Huh? What the heck is {params.movieId}?
        </div>
      );
    }
    case 401: {
      return (
        <div className="error-container">
          Sorry, but {params.movie} is not yours.
        </div>
      );
    }
    default: {
      throw new Error(`Unhandled error: ${caught.status}`);
    }
  }
}

export function ErrorBoundary({ error }: { error: Error }) {
  console.error(error);

  const { movieId } = useParams();
  return (
    <div className="error-container">{`There was an error loading movie by the id ${movieId}. Sorry.`}</div>
  );
}