<script lang="ts">
	import { Trigger } from '$lib/components/ui/sheet'
	import Navigator from './Navigator.svelte'
	import { Button } from './ui/button'
	import { Separator } from './ui/separator'
</script>

<div class="flex h-screen w-full flex-col space-y-3 p-3">
	<div class="flex w-full basis-auto items-center space-x-2">
		<slot name="header" />
	</div>
	<Separator />
	<div class="w-full basis-full"><slot name="content" /></div>
</div>
