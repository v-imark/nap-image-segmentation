<script lang="ts">
	import { writable } from "svelte/store"
	import { Label } from "./ui/label"
    import { Slider } from "./ui/slider"

    export let value = writable<number>()
    export let label: string
    export let min = 0
    export let max = 100
    export let step = 1

    let val: number[] = [$value]

    $: value.set(val[0])
</script>

<div class="flex flex-col space-y-1.5">
    <div class="flex justify-between">
        <Label>{label}</Label>
        <Label>{val}</Label>
    </div>
    <Slider bind:value={val} min={min} max={max} step={step}/>
</div>
