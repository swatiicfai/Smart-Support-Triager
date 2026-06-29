function fillHappyPath() {
    document.getElementById('email-address').value = "john.doe@example.com";
    document.getElementById('email-content').value = "Hi, can you tell me the status of ORD-1234? Thanks!";
}

function fillExceptionPath() {
    document.getElementById('email-address').value = "angry.customer@example.com";
    document.getElementById('email-content').value = "This is ridiculous! I've been waiting forever for ORD-9999. I want a refund now!";
}

function sleep(ms) {
    return new Promise(resolve => setTimeout(resolve, ms));
}

function resetUI() {
    document.getElementById('step-ai').classList.remove('active');
    document.getElementById('step-gateway').classList.remove('active');
    document.getElementById('step-action').classList.remove('active');
    
    document.getElementById('conn-1').classList.remove('active');
    document.getElementById('conn-2').classList.remove('active');

    document.querySelector('#step-ai .status-text').className = "status-text waiting";
    document.querySelector('#step-ai .status-text').innerText = "Waiting for input...";
    document.getElementById('ai-json').classList.add('hidden');

    document.querySelector('#step-gateway .status-text').className = "status-text waiting";
    document.querySelector('#step-gateway .status-text').innerText = "Waiting for classification...";

    document.querySelector('#step-action .status-text').className = "status-text waiting";
    document.querySelector('#step-action .status-text').innerText = "Waiting for routing...";
    document.getElementById('action-card').classList.add('hidden');
    
    // Reset colors
    document.querySelector('#step-gateway .step-icon').style.background = "";
    document.querySelector('#step-action .step-icon').style.background = "";
}

document.getElementById('run-btn').addEventListener('click', async () => {
    const text = document.getElementById('email-content').value.toLowerCase();
    const btn = document.getElementById('run-btn');
    
    // UI Loading state
    btn.disabled = true;
    btn.innerHTML = '<i class="fa-solid fa-spinner fa-spin"></i> Processing...';
    
    resetUI();

    // Determine path based on text
    const isAngry = text.includes('ridiculous') || text.includes('refund');

    // === STEP 1: AI Agent ===
    document.getElementById('step-ai').classList.add('active');
    const aiStatus = document.querySelector('#step-ai .status-text');
    aiStatus.className = "status-text processing";
    aiStatus.innerHTML = '<i class="fa-solid fa-circle-notch fa-spin"></i> Analyzing intent and sentiment...';
    
    await sleep(1500); // Simulate API call
    
    let mockJSON;
    if (isAngry) {
        mockJSON = {
            "intent": "refund_request",
            "sentiment": "angry",
            "urgency": "high"
        };
    } else {
        mockJSON = {
            "intent": "order_status",
            "sentiment": "neutral",
            "urgency": "low"
        };
    }

    aiStatus.className = "status-text success";
    aiStatus.innerHTML = '<i class="fa-solid fa-check"></i> Classification Complete';
    
    const jsonBox = document.getElementById('ai-json');
    jsonBox.innerText = JSON.stringify(mockJSON, null, 2);
    jsonBox.classList.remove('hidden');

    await sleep(800);
    document.getElementById('conn-1').classList.add('active');

    // === STEP 2: Gateway ===
    document.getElementById('step-gateway').classList.add('active');
    const gwStatus = document.querySelector('#step-gateway .status-text');
    gwStatus.className = "status-text processing";
    gwStatus.innerHTML = '<i class="fa-solid fa-circle-notch fa-spin"></i> Evaluating routing rules...';

    await sleep(1000);

    if (isAngry) {
        gwStatus.className = "status-text error";
        gwStatus.innerHTML = '<i class="fa-solid fa-code-branch"></i> Route: Escalate to Human Agent (Exception Path)';
        document.querySelector('#step-gateway .step-icon').style.background = "var(--danger)";
        document.querySelector('#step-gateway .step-icon').style.borderColor = "var(--danger)";
    } else {
        gwStatus.className = "status-text success";
        gwStatus.innerHTML = '<i class="fa-solid fa-code-branch"></i> Route: Automated Response (Happy Path)';
        document.querySelector('#step-gateway .step-icon').style.background = "var(--success)";
        document.querySelector('#step-gateway .step-icon').style.borderColor = "var(--success)";
    }

    await sleep(800);
    document.getElementById('conn-2').classList.add('active');

    // === STEP 3: Action ===
    document.getElementById('step-action').classList.add('active');
    const actionTitle = document.getElementById('action-title');
    const actionStatus = document.querySelector('#step-action .status-text');
    const actionCard = document.getElementById('action-card');
    
    if (isAngry) {
        actionTitle.innerText = "3. Action Center Handoff";
        actionStatus.className = "status-text processing";
        actionStatus.innerHTML = '<i class="fa-solid fa-circle-notch fa-spin"></i> Creating High-Priority Case...';
        document.querySelector('#step-action .step-icon').innerHTML = '<i class="fa-solid fa-user-shield"></i>';
        document.querySelector('#step-action .step-icon').style.background = "var(--danger)";

        await sleep(1200);

        actionStatus.className = "status-text error";
        actionStatus.innerHTML = '<i class="fa-solid fa-triangle-exclamation"></i> Case Escalated to Human';
        
        actionCard.innerHTML = `
            <div style="color: var(--danger); font-weight: bold; margin-bottom: 0.5rem;">UiPath Action Center</div>
            <div><strong>Priority:</strong> High</div>
            <div><strong>Intent:</strong> refund_request</div>
            <div><strong>Sentiment:</strong> angry</div>
            <div style="margin-top: 0.5rem; font-size: 0.8rem; color: var(--text-muted);">Status: Waiting for Human Review</div>
        `;
        actionCard.classList.remove('hidden');

    } else {
        actionTitle.innerText = "3. RPA Database Lookup";
        actionStatus.className = "status-text processing";
        actionStatus.innerHTML = '<i class="fa-solid fa-circle-notch fa-spin"></i> Checking Database for ORD-1234...';
        document.querySelector('#step-action .step-icon').innerHTML = '<i class="fa-solid fa-database"></i>';
        document.querySelector('#step-action .step-icon').style.background = "var(--success)";

        await sleep(1200);

        actionStatus.className = "status-text success";
        actionStatus.innerHTML = '<i class="fa-solid fa-check"></i> Automated Reply Sent';
        
        actionCard.innerHTML = `
            <div style="color: var(--success); font-weight: bold; margin-bottom: 0.5rem;">Drafted Email</div>
            <div style="font-style: italic;">"Hello, your order ORD-1234 is currently Shipped. Expected delivery is 2026-07-02."</div>
        `;
        actionCard.classList.remove('hidden');
    }

    // Reset button
    btn.disabled = false;
    btn.innerHTML = '<span>Run Agentic Workflow</span> <i class="fa-solid fa-arrow-right"></i>';
});
