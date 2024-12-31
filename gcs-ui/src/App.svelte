<script lang="ts">
  import "leaflet/dist/leaflet.css";
  import "./app.css";
  import Map from "./Map.svelte";
  import Footer from "./Footer.svelte";
</script>

<div class="flex flex-col h-screen">
  <div class="flex-1 relative">
    <Map />
  </div>

  <Footer />
</div>
