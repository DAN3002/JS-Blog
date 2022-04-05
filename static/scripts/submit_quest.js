const getUrlParameter = (key) => {
	const urlParams = new URLSearchParams(window.location.search);
	return urlParams.get(key);
}

document.addEventListener("DOMContentLoaded", function (event) {
	const submitQuestBtn = document.getElementById('submit-quest-btn');
	const questPasswordInput = document.getElementById('quest-password-input');

	submitQuestBtn.addEventListener('click', function (event) {
		event.preventDefault();

		const questPassword = questPasswordInput.value;

		if (!questPassword) {
			// Alert swal
			Swal.fire({
				title: 'Error',
				text: 'Please enter a password',
				icon: 'error',
				button: 'Ok'
			});
		}
		// Clear input
		questPasswordInput.value = '';

		// get type in url parram
		const type = getUrlParameter('type');

		const data = {
			quest_password: questPassword,
			type: type
		}

		fetch("/quest/submit_quest", {
			method: "POST",
			body: JSON.stringify(data)
		}).then(async (res) => {
			const data = await res.json();

			const { status, next_quest } = data

			if (status === 'success') {
				// Alert swal
				Swal.fire({
					title: 'Success',
					text: 'Quest submitted successfully',
					icon: 'success',
					button: 'Ok'
				}).then(() => {
					if (next_quest) {
						window.location.href = `/quest?type=${ next_quest }`;
					}
				});
			}
			else {
				// Alert swal
				Swal.fire({
					title: 'Error',
					text: 'Incorrect password',
					icon: 'error',
					button: 'Ok'
				});
			}
		});
	});
});
