<script lang="ts">
	export let map: string
</script>

<div class="flex h-full w-full items-stretch overflow-clip rounded-full">
	{#each { length: 20 } as _, i}
		<div class="w-[5%] bg-{map}-default-{i}"></div>
	{/each}
</div>
