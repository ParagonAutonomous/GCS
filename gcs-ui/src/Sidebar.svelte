<script lang="ts">
  import { Button } from "flowbite-svelte";
  import {
    ChartPieSolid,
    ClipboardSolid,
    CogSolid,
    FireSolid,
    MapPinAltSolid,
    PaperPlaneSolid,
  } from "flowbite-svelte-icons";
  import { currentPage } from "./store";
</script>

<div class="w-44 bg-white flex flex-col space-y-2 p-2">
  <Button
    size="md"
    color={$currentPage === "Dashboard" ? "blue" : "alternative"}
    on:click={() => currentPage.set("Dashboard")}
    class="justify-start"
  >
    <ChartPieSolid class="w-5 h-5 me-2" />
    Dashboard
  </Button>
  <Button
    size="md"
    color={$currentPage === "Drones" ? "blue" : "alternative"}
    on:click={() => currentPage.set("Drones")}
    class="justify-start"
  >
    <PaperPlaneSolid class="w-5 h-5 me-2" />
    Drones
  </Button>
  <Button
    size="md"
    color={$currentPage === "Mapping" ? "blue" : "alternative"}
    on:click={() => currentPage.set("Mapping")}
    class="justify-start"
  >
    <MapPinAltSolid class="w-5 h-5 me-2" />
    Mapping
  </Button>
  <Button
    size="md"
    color={$currentPage === "Missions" ? "blue" : "alternative"}
    on:click={() => currentPage.set("Missions")}
    class="justify-start"
  >
    <ClipboardSolid class="w-5 h-5 me-2" />
    Missions
  </Button>
  <Button
    size="md"
    color={$currentPage === "Events" ? "blue" : "alternative"}
    on:click={() => currentPage.set("Events")}
    class="justify-start"
  >
    <FireSolid class="w-5 h-5 me-2" />
    Events
  </Button>
  <Button
    size="md"
    color={$currentPage === "Settings" ? "blue" : "alternative"}
    on:click={() => currentPage.set("Settings")}
    class="justify-start"
  >
    <CogSolid class="w-5 h-5 me-2" />
    Settings
  </Button>
</div>
