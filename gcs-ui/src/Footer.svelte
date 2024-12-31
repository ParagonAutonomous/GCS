<script lang="ts">
  import { onMount } from "svelte";
  import { writable } from "svelte/store";
  import version from "./versionStore";

  const serverStatus = writable<string>("checking");
  const statusColor = writable<string>("bg-gray-400");

  const gcsCoreUrl = import.meta.env.VITE_GCS_CORE_URL;

  onMount(async () => {
    try {
      const response = await fetch(`${gcsCoreUrl}/status`);
      if (response.ok) {
        serverStatus.set("running");
        statusColor.set("bg-green-500");
      } else {
        serverStatus.set("not running");
        statusColor.set("bg-red-500");
      }
    } catch (error) {
      serverStatus.set("not running");
      statusColor.set("bg-red-500");
    }
  });
</script>

<div
  class="bg-gray-100 shadow-md flex items-center justify-between p-1 text-xs h-6"
>
  <div class="flex items-center space-x-2 pl-1">
    <div class={`h-2 w-2 rounded-full ${$statusColor}`}></div>
    <span>GCS: {$serverStatus}</span>
  </div>
  <div>
    v{$version}
  </div>
</div>
