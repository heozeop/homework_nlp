import { PrismaClient } from "@prisma/client";
import fs from 'fs';
import path from 'path';

const db = new PrismaClient();

const genres = ['Action', 'Adventure', 'Animation', 'Comedy', 'Crime', 'Drama', 'Family', 'Fantasy', 'Film-Noir', 'Horror', 'Musical', 'Mystery', 'Romance', 'Sci-Fi', 'Short', 'Thriller', 'War', 'Western']
const imgSrouce = "https://www.imsdb.com"

async function seed() {
  const genreList = await Promise.all(
    genres.map(genre => db.genre.create({ data: { name: genre }}))
  )

  const movieInfo = getMovieData().map(movie => ({...movie, title: movie.title.replace(', The', '')}))
  // author
  const uniqAuthors = [...new Set(movieInfo.flatMap(
      movie => movie.authors
    ))]

  const authors = await Promise.all(uniqAuthors.map(author => db.author.create({
    data: { name: author }
  })));
  // Movies
  const movies = await Promise.all(
    movieInfo.map(movieInfo => db.movie.create({
      data: {
        title: movieInfo['title'],
        poster: imgSrouce + movieInfo['imgSrc'] || '',
    }}))
  )

  // prepare to make relations

  const authorMap = new Map<string, string>();
  authors.forEach(data => {
    authorMap.set(data.name, data.id)
  })

  const genreMap = new Map<string, string>()
  genreList.forEach(data => {
    genreMap.set(data.name, data.id);
  })

  const movieMap = new Map<string, string>();
  movies.forEach(data => {
    movieMap.set(data.title, data.id)
  })

  // Author to Movie
  await Promise.all(movieInfo.flatMap(movie => {
      const movieId = movieMap.get(movie.title)
      if (movieId) {
        return movie.authors.map(author => {
          const authorId = authorMap.get(author)
          if (authorId && movieId) {
              return db.authorsOnMovie.create({
                data: {
                  authorId:authorId,
                  movieId: movieId
                }
              })
            }
        })
      }
  }))

  // genres to movies
  await Promise.all(movieInfo.flatMap(movie => {
    const movieId = movieMap.get(movie.title)
    if (movieId) {
      return movie.genres.map(genre => {
        const genreId = genreMap.get(genre)
        if (genreId && movieId) {
          return db.genresOnMovie.create({
            data: {
              genreId: genreId,
              movieId: movieId,
          }})
        }
      })
    }
  }))

}

seed();

function getMovieData(): Array<{ 
  imgSrc: string | null;
  title: string;
  genres: Array<string>;
  authors: Array<string>;
}> {
  const file = fs.readFileSync(path.resolve(__dirname,'../data/movie_default.json'), 'utf8')
  return JSON.parse(file);
}
