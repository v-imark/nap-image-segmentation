<script lang="ts">
	import ParamSelector from '$lib/components/ParamSelector.svelte'
	import Separator from '$lib/components/ui/separator/separator.svelte'
</script>

<div class="flex h-full flex-row items-stretch py-3">
	<div class="basis-1/6 px-3">
		<ParamSelector />
	</div>
	<Separator orientation="vertical" />
	<div class="flex basis-3/6 flex-col p-3"></div>
	<Separator orientation="vertical" />
	<div class="flex basis-2/6 flex-col p-3"></div>
</div>
