document.addEventListener('DOMContentLoaded', () => {
    const loanApplicationForm = document.getElementById('loanApplicationForm');
    const apiUrl = 'http://'; // Adjust based on your backend URL

    loanApplicationForm.addEventListener('submit', async (event) => {
        event.preventDefault();
        const title = document.getElementById('title').value;
        const firstName = document.getElementById('firstName').value;
        const lastName = document.getElementById('lastName').value;
        const dob = document.getElementById('dob').value;
        const phoneNumber = document.getElementById('phoneNumber').value;
        const username = document.getElementById('username').value;
        const email = document.getElementById('email').value;
        const idType = document.getElementById('idType').value;
        const address = document.getElementById('address').value;
        const city = document.getElementById('city').value;
        const state = document.getElementById('state').value;
        const postalCode = document.getElementById('postalCode').value;
        const bankName = document.getElementById('bankName').value;
        const accountNumber = document.getElementById('accountNumber').value;
        const accountType = document.querySelector('input[name="accountType"]:checked').value;
        const loanPurpose = document.querySelector('input[name="loanPurpose"]:checked').value;
        const amount = document.getElementById('loanAmount').value;
        const term = document.getElementById('loanTerm').value;

        const response = await fetch(`${apiUrl}/loan-application`, {
            method: 'POST',
            headers: { 'Content-Type': 'application/json' },
            body: JSON.stringify({
                title, firstName, lastName, dob, phoneNumber, username,
                email, idType, address, city, state, postalCode, bankName, accountNumber, accountType, loanPurpose, amount, term
            })
        });

        const data = await response.json();
        alert(data.message);
    });
});
