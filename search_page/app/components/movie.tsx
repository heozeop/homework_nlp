import type { Movie } from "@prisma/client";

export function MoviePosterItem({
  movie,
}: {
  movie: Movie
}) {
  return (
    <div className="w-full">
      <div className="aspect-[100/148] w-full">
        <img className="object-fill w-full h-full" src={movie.poster} alt={movie.title}></img>
      </div>
      <p className="w-full text-ellipsis whitespace-nowrap overflow-hidden">{movie.title}</p>
    </div>
  );
}

