let allVoices = [];

const speed = document.getElementById("speed");
const speedValue = document.getElementById("speedValue");

speed.addEventListener("input", () => {
    speedValue.textContent = speed.value;
});

// ----------------------------
// Load Voices
// ----------------------------
async function loadVoices() {

    const response = await fetch("/static/voices.json");

    allVoices = await response.json();

    populateLanguages();
}

// ----------------------------
// Populate Languages
// ----------------------------
function populateLanguages() {

    const languageSelect = document.getElementById("language");

    languageSelect.innerHTML = "";

    // Get unique languages
    const languages = [...new Set(allVoices.map(v => v.language))];

    languages.sort();

    languages.forEach(language => {

        const option = document.createElement("option");

        option.value = language;
        option.textContent = language;

        languageSelect.appendChild(option);

    });

    languageSelect.addEventListener("change", populateVoices);

    populateVoices();
}

// ----------------------------
// Populate Voices
// ----------------------------
function populateVoices() {

    const language = document.getElementById("language").value;

    const voiceSelect = document.getElementById("voice");

    voiceSelect.innerHTML = "";

    const voices = allVoices.filter(v => v.language === language);

    voices.forEach(v => {

        const option = document.createElement("option");

        option.value = v.id;

        option.dataset.lang = v.lang;

        option.textContent = `${v.name} (${v.gender})`;

        voiceSelect.appendChild(option);

    });

}

// ----------------------------
// Generate Speech
// ----------------------------
async function generateVoice() {

    const text = document.getElementById("text").value.trim();

    if (text.length === 0) {

        alert("Please enter some text.");

        return;

    }

    const voiceSelect = document.getElementById("voice");

    const selectedOption = voiceSelect.options[voiceSelect.selectedIndex];

    const result = document.getElementById("result");

    result.innerHTML = `
        <div class="skeleton-audio"></div>
        <div class="skeleton-icon"></div>
    `;

    const response = await fetch("/generate", {

        method: "POST",

        headers: {

            "Content-Type": "application/json"

        },

        body: JSON.stringify({

            text: text,

            voice: selectedOption.value,

            lang: selectedOption.dataset.lang,

            speed: speed.value

        })

    });

    const data = await response.json();

    if (!data.success) {

        result.innerHTML = "<p>Generation failed.</p>";

        return;

    }

    result.innerHTML = `
            <audio controls src="/audio/${data.filename}"></audio>
            <a href="/download/${data.filename}" class="download-icon" title="Download WAV" download>⬇️</a>
        `;

}

// ----------------------------

loadVoices();