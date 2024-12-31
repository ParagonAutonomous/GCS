import { defineConfig } from "vite";
import { svelte } from "@sveltejs/vite-plugin-svelte";
import dotenv from "dotenv";

dotenv.config();

export default defineConfig({
  plugins: [svelte()],
  server: {
    port: 3030,
    host: true, // This allows the server to be accessible externally
  },
});
