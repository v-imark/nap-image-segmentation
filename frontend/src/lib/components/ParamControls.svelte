<script lang="ts">
	import { SEGMENTATION_PARAMS } from '../../stores'
	import SliderWithLabel from './SliderWithLabel.svelte'

	let params = Object.entries(SEGMENTATION_PARAMS)
</script>

<div class="m-3 flex flex-col space-y-3">
	{#each params as [key, param]}
		<SliderWithLabel
			label={key}
			value={param.writable}
			min={param.min}
			max={param.max}
			step={param.step}
		/>
	{/each}
</div>
