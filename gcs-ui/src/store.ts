import { writable } from "svelte/store";

const version = writable<string>("");
const currentPage = writable<string>("Dashboard");

fetch("/package.json")
  .then((response) => response.json())
  .then((data) => {
    version.set(data.version);
  });

export { version, currentPage };
