export async function searchApi({ text }: {text?: string}) {
  let apiUrl = "http://api.example.com/some-data.json";
  if (process.env.NODE_ENV !== 'production') {
    apiUrl = 'http://127.0.0.1:8000/search';
  }

  if (text) {
    apiUrl += `?text=${text}`;
  }

  let res = await fetch(apiUrl);

  let data: {emotion: string, movies: string[]} = await res.json();

  return data;
}