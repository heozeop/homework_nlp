import type { Movie } from "@prisma/client";

export function MovieDisplay({
  movie,
}: {
  movie: Movie
}) {
  return (
    <div>
      <p>{movie.title}</p>
      <img src={movie.poster} alt={movie.title}></img>
    </div>
  );
}