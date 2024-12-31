<script lang="ts">
  import { onMount } from "svelte";
  import L from "leaflet";

  let map;

  onMount(() => {
    map = L.map("map").setView([33.420947637373956, -111.93400715847837], 13);
    L.tileLayer("https://{s}.tile.openstreetmap.org/{z}/{x}/{y}.png", {
      attribution:
        '&copy; <a href="https://www.openstreetmap.org/copyright">OpenStreetMap</a> contributors',
    }).addTo(map);

    L.marker([33.420947637373956, -111.93400715847837])
      .addTo(map)
      .bindPopup("Waypoint 1")
      .openPopup();
  });
</script>

<div id="map" class="h-full w-full"></div>
