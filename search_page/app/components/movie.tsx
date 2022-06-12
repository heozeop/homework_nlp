import type { Movie } from "@prisma/client";

export function MovieDisplay({
  movie,
}: {
  movie: Movie
}) {
  return (
    <div className="w-full">
      <img src={movie.poster} alt={movie.title}></img>
      <p className="text-ellipsis">{movie.title}</p>
    </div>
  );
}

