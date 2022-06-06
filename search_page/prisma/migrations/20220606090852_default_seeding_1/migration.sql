/*
  Warnings:

  - You are about to drop the `Joke` table. If the table is not empty, all the data it contains will be lost.

*/
-- DropTable
PRAGMA foreign_keys=off;
DROP TABLE "Joke";
PRAGMA foreign_keys=on;

-- CreateTable
CREATE TABLE "Genre" (
    "id" TEXT NOT NULL PRIMARY KEY,
    "name" TEXT NOT NULL
);

-- CreateTable
CREATE TABLE "Author" (
    "id" TEXT NOT NULL PRIMARY KEY,
    "name" TEXT NOT NULL,
    "createdAt" DATETIME NOT NULL DEFAULT CURRENT_TIMESTAMP,
    "updatedAt" DATETIME NOT NULL
);

-- CreateTable
CREATE TABLE "Movie" (
    "id" TEXT NOT NULL PRIMARY KEY,
    "createdAt" DATETIME NOT NULL DEFAULT CURRENT_TIMESTAMP,
    "updatedAt" DATETIME NOT NULL,
    "title" TEXT NOT NULL,
    "poster" TEXT NOT NULL
);

-- CreateTable
CREATE TABLE "GenresOnMovie" (
    "genreId" TEXT NOT NULL,
    "movieId" TEXT NOT NULL,
    "assignedAt" DATETIME NOT NULL DEFAULT CURRENT_TIMESTAMP,

    PRIMARY KEY ("genreId", "movieId"),
    CONSTRAINT "GenresOnMovie_genreId_fkey" FOREIGN KEY ("genreId") REFERENCES "Genre" ("id") ON DELETE CASCADE ON UPDATE CASCADE,
    CONSTRAINT "GenresOnMovie_movieId_fkey" FOREIGN KEY ("movieId") REFERENCES "Movie" ("id") ON DELETE CASCADE ON UPDATE CASCADE
);

-- CreateTable
CREATE TABLE "AuthorsOnMovie" (
    "authorId" TEXT NOT NULL,
    "movieId" TEXT NOT NULL,

    PRIMARY KEY ("authorId", "movieId"),
    CONSTRAINT "AuthorsOnMovie_authorId_fkey" FOREIGN KEY ("authorId") REFERENCES "Author" ("id") ON DELETE CASCADE ON UPDATE CASCADE,
    CONSTRAINT "AuthorsOnMovie_movieId_fkey" FOREIGN KEY ("movieId") REFERENCES "Movie" ("id") ON DELETE CASCADE ON UPDATE CASCADE
);

-- CreateIndex
CREATE UNIQUE INDEX "Genre_name_key" ON "Genre"("name");

-- CreateIndex
CREATE UNIQUE INDEX "Author_name_key" ON "Author"("name");
