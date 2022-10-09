const sentenceEls = document.querySelectorAll(".sentence");
const popUp = document.getElementById("pop-up");
const imgLabel = document.querySelector(".custom-upload");
const sentenceList = document.querySelector(".sentence-list");

/*------------------------------------*\
  #EVENT-HANDLERS
\*------------------------------------*/

async function copyToClipboard(event) {
	const password = event.target.textContent;
	try {
		await navigator.clipboard.writeText(password);
	} catch (err) {
		console.log("Clipboard access denied. Time to go old school...");
		copyUsingExecCommand(password);
	}

	// show a pop-up to notify the user
	clearTimeout(timeoutId);
	popUp.style.opacity = 0.9;
	timeoutId = setTimeout(() => (popUp.style.opacity = 0), 1000);
}

function copyUsingExecCommand(text) {
	const input = document.createElement("input");
	input.value = text;
	input.readOnly = true;
	input.style = {
		position: "absolute",
		left: "-9999px",
	};
	document.body.append(input);
	input.select();
	document.execCommand("copy");
	input.remove();
}

function loadImg() {
	const selectedFile = document.getElementById("img-upload").files[0];
	console.log("1");
	const reader = new FileReader();
	reader.addEventListener("load", () => {
		const uploaded_image = reader.result;
		const displayImg = document.querySelector("#display-image");
		displayImg.classList.remove("hidden");
		displayImg.style.backgroundImage = `url(${uploaded_image})`;
	});
	reader.readAsDataURL(selectedFile);

	loadSentences(selectedFile);
}

function loadSentences(img) {
	// upload image
	let formData = new FormData();
	formData.append("file", img);
	const requestOptions = {
		headers: {
			"Content-Type": img.contentType,
		},
		mode: "no-cors",
		method: "POST",
		files: img,
		body: formData,
	};

	// run python
	fetch("http://127.0.0.1:5000/upload", requestOptions).then((response) => {
		// load sentences
		jsonData = response;
		console.log(jsonData);
		listSentences(jsonData);
	});
}

function listSentences(json) {
	const title1 = document.createElement("li");
	title1.textContent = "Google Cloud OCR: ";
	const title2 = document.createElement("li");
	title2.textContent = "Formatted Text: ";
	sentenceList.append(title1, title2);

	return json.map((item) => {
		const orig_text = document.createElement("li");
		const new_text = document.createElement("li");

		orig_text.textContent = Object.values(item)[0];
		new_text.textContent = Object.values(item)[0];

		orig_text.classList.add("sentence");
		new_text.classList.add("sentence");

		sentenceList.append(orig_text, new_text);
		return sentenceList;
	});
}

// Initialize
let timeoutId;

// event listeners
sentenceEls.forEach((element) => {
	element.addEventListener("click", copyToClipboard);
});

imgLabel.addEventListener("change", loadImg);
