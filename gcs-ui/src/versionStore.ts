import { writable } from "svelte/store";

const version = writable<string>("");

fetch("/package.json")
  .then((response) => response.json())
  .then((data) => {
    version.set(data.version);
  });

export default version;
