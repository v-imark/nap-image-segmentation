<script lang="ts">
	import { cn } from '$lib/utils'
	import { resetStore } from '../../stores'
	import { Button } from './ui/button'

	let className: string | undefined = undefined

	export { className as class }
</script>

<div class={cn('flex flex-row justify-center space-x-1', className)}>
	<Button>Compute Masks</Button>
	<Button variant="secondary" on:click={resetStore}>Reset</Button>
</div>
