<script lang="ts">
  import { onMount } from "svelte";
  import L from "leaflet";

  let map;

  onMount(() => {
    map = L.map("map", {
      zoomControl: false,
    }).setView([33.420947637373956, -111.93400715847837], 13);
    L.tileLayer("https://{s}.tile.openstreetmap.org/{z}/{x}/{y}.png", {
      attribution:
        '&copy; <a href="https://www.openstreetmap.org/copyright">OpenStreetMap</a> contributors',
    }).addTo(map);

    L.control.zoom({ position: "bottomright" }).addTo(map);
  });
</script>

<div id="map" class="h-full w-full"></div>
