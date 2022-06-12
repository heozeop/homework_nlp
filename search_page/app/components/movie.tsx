import type { Movie } from "@prisma/client";
import { useState } from "react";

export function MoviePosterItem({
  movie,
}: {
  movie: Movie & {
    genres: string[];
}
}) {
  const [imageSrc, setImageSrc] = useState(movie.poster)
  

  return (
    <div className="w-full">
      <div className="aspect-[100/148] w-full">
        <img
          className="object-fill w-full h-full"
          src={imageSrc}
          onError={(e) => {
            if (imageSrc && movie.poster === imageSrc) {
              setImageSrc("https://imsdb.com/images/no-poster.gif")
            }
          }}
          alt={movie.title}></img>
      </div>
      <p className="text-xl w-full text-ellipsis whitespace-nowrap overflow-hidden">{movie.title}</p>
      <p className="text-sm w-full text-ellipsis whitespace-nowrap overflow-hidden">{movie.genres.join(', ')}</p>
    </div>
  );
}

