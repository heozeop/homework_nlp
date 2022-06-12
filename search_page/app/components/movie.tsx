import type { Movie } from "@prisma/client";

export function MoviePosterItem({
  movie,
}: {
  movie: Movie & {
    genres: string[];
}
}) {
  return (
    <div className="w-full">
      <div className="aspect-[100/148] w-full">
        <img className="object-fill w-full h-full" src={movie.poster} alt={movie.title}></img>
      </div>
      <p className="text-xl w-full text-ellipsis whitespace-nowrap overflow-hidden">{movie.title}</p>
      <p className="text-sm w-full text-ellipsis whitespace-nowrap overflow-hidden">{movie.genres.join(', ')}</p>
    </div>
  );
}

