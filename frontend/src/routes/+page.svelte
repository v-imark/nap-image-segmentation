<script lang="ts">
	import MainPage from '$lib/components/MainPage.svelte'
	import Navigator from '$lib/components/Navigator.svelte'
	import type { PageData } from './$types'

	export let data: PageData
</script>

<!-- <MainPage /> -->
<div class="flex h-full w-full items-center justify-center">
	<Navigator />
</div>
