document.addEventListener("DOMContentLoaded", function (event) {
	const submitQuestBtn = document.getElementById('check_password_button');
	const questPasswordInput = document.getElementById('password');

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
		const data = {
			quest_password: questPassword,
		}


		fetch("/quest/check_pass", {
			method: "POST",
			body: JSON.stringify(data),
		}).then(async (res) => {
			const data = await res.json();

			const { status } = data

			if (status === 'success') {
				// Alert swal
				Swal.fire({
					title: 'Success',
					text: 'Correct Password!',
					icon: 'success',
					button: 'Ok'
				}).then(() => {
					// if (next_quest) {
					// 	window.location.href = `/quest?type=${ next_quest }`;
					// }
				});
			}
			else {
				// Alert swal
				Swal.fire({
					title: 'Error',
					text: 'Incorrect password!',
					icon: 'error',
					button: 'Ok'
				});
			}
		});
	});
});
