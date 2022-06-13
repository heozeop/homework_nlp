export type TSearchResult = 
  { emotion: string; movies: string[]; genre: string; }

export async function searchApi({ text }: {text?: string}) {
  let apiUrl = "https://imsdb-searcher-api.fly.dev/search";
  if (process.env.NODE_ENV !== 'production') {
    apiUrl = 'http://127.0.0.1:8000/search';
  }

  if (text) {
    apiUrl += `?text=${text}`;
  }

  let res = await fetch(apiUrl);

  let data: TSearchResult = await res.json();

  return data;
}