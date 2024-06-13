<script>
	import '../app.pcss'
	import * as Sheet from '$lib/components/ui/sheet'
	import Navigator from '$lib/components/Navigator.svelte'
	import Separator from '$lib/components/ui/separator/separator.svelte'
</script>

<div class="flex h-screen w-full flex-col">
	<div class="bg-primary w-full basis-auto px-3 pt-1">
		<Navigator />
	</div>
	<slot />
</div>
