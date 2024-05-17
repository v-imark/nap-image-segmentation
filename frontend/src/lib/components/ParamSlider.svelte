<script lang="ts">
	import { Label } from './ui/label'
	import { Slider } from './ui/slider'

	export let value
	export let label: string
	export let maxMinStep: { max: number; min: number; step: number; disable: boolean }

	let sliderVal = [value]
	$: value = sliderVal[0]
</script>

<div class="flex w-full flex-col items-center space-y-1">
	<div class="flex w-full justify-between">
		<Label class="w-12">{label}</Label>
		<Label class="w-12 text-right">{sliderVal[0]}</Label>
	</div>
	<Slider
		bind:value={sliderVal}
		min={maxMinStep.min}
		max={maxMinStep.max}
		step={maxMinStep.step}
		disabled={maxMinStep.disable}
	></Slider>
</div>
