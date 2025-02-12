const express = require('express');
const { execFile } = require('child_process');

const app = express();
app.use(express.urlencoded({ extended: true }));

// Allow only valid domain names or IPs
function isValidHost(host) {
    const ipRegex = /^(?:\d{1,3}\.){3}\d{1,3}$/; // Matches IPv4
    const domainRegex = /^(?!-)[a-zA-Z0-9.-]{1,253}(?<!-)$/; // Matches domain names
    return ipRegex.test(host) || domainRegex.test(host);
}

app.get('/', (req, res) => {
    res.send(`
        <h1>Ping a Website</h1>
        <form method="POST" action="/ping">
            <label for="host">Enter a hostname or IP address:</label>
            <input type="text" id="host" name="host" placeholder="e.g., google.com">
            <button type="submit">Ping</button>
        </form>
    `);
});

app.post('/ping', (req, res) => {
    const host = req.body.host.trim();

    if (!isValidHost(host)) {
        return res.send("Invalid input. Please enter a valid hostname or IP.");
    }

    execFile('ping', ['-c', '4', host], (error, stdout, stderr) => {
        if (error) {
            return res.send(`Error: ${stderr}`);
        }
        res.send(`<pre>${stdout}</pre>`);
    });
});

app.listen(3000, () => {
    console.log('Secure ping app running on http://localhost:3000');
});
