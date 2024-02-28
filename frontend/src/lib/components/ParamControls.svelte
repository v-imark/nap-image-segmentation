<script lang="ts">
	import { SEGMENTATION_PARAMS } from "../../constants"
    import SliderWithLabel  from "./SliderWithLabel.svelte"

    let params = Object.entries(SEGMENTATION_PARAMS)
</script>

<div class="flex flex-col space-y-3 m-3">
    {#each params as [key, param]}
        <SliderWithLabel label={key} value={param.writable} min={param.min} max={param.max} step={param.step}/>
    {/each}
</div>
