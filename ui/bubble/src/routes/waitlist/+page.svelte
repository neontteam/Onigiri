<script lang="ts">
    import { onMount } from 'svelte';

    let email: string = "";
    let msg: string = "";
    let randomColor: string = "";

    onMount(set_background_color);

    function set_background_color() {
        const colors = ["bg-blue-100", "bg-red-100", "bg-green-100", "bg-purple-100", "bg-yellow-100"];
        randomColor = colors[Math.floor(Math.random() * colors.length)];
        console.log(randomColor);
    }

    async function subscribe_to_waitlist() {
        msg = "Clicked on subscribe button";
        try {
            const response = await fetch('http://127.0.0.1:8000/waitlist/subscribe', {
                method: 'POST',
                headers: {
                    'Content-Type': 'application/json',
                },
                body: JSON.stringify({ email: email }),
            });
            if (response.status == 200) {
                msg = "<span style='color: green'>Subscribed successfully</span>";
                return;
            }
            if (response.status == 422) {
                msg = "<span style='color: red'>Invalid email. Please check!</span>";
                return;
            }
            const data = await response.json();
            msg = `<span style='color: red'>${data['msg']}</span>`;
        } catch (error) {
            console.log(error);
            msg = "<span style='color: red'>Unknown error occurred. Please try again later.</span>";
        }

    }
</script>
<link href="https://fonts.googleapis.com/css2?family=Roboto:wght@400;700&display=swap" rel="stylesheet">
<link href="https://cdn.jsdelivr.net/npm/tailwindcss@2.2.19/dist/tailwind.min.css" rel="stylesheet">
<div class="flex items-center justify-center h-screen {randomColor}" on:load={set_background_color}>
    <div class="bg-white shadow-md rounded px-8 pt-6 pb-8 mb-4 flex flex-col">
        <div class="mb-4">
            <h1 class="font-bold text-2xl mb-2 text-gray-700">Coming Soon</h1>
        </div>
        <form>
            <div class="mb-4">
                <input bind:value={email} class="shadow appearance-none border rounded w-full py-2 px-3 text-gray-700 leading-tight focus:outline-none focus:shadow-outline" id="email" type="text" placeholder="Email ID">
            </div>
            <div class="flex items-center justify-between">
                <button class="bg-blue-500 hover:bg-blue-700 text-white font-bold py-2 px-4 rounded focus:outline-none focus:shadow-outline" on:click={subscribe_to_waitlist}>
                    Subscribe
                </button>
            </div>
        </form>
        <br>
        <span id="message_banner" class="text-gray-700 text-xs">{@html msg}</span>
    </div>
</div>