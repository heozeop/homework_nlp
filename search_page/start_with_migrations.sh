#!/bin/sh

set -ex
npx prisma migrate deploy
npx prisma migrate reset --force
npm run start
