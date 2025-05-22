//AI generated javascript code
// this is a python class not web development and design i dont think im supposed to know how to do this//


function openGoogleCalendar() {
    window.open('https://calendar.google.com/', '_blank');
}

// Timer functionality
document.addEventListener('DOMContentLoaded', function() {
    // Get the initial timer value
    const timerDisplay = document.getElementById('countdown-timer');
    let initialTime = timerDisplay.textContent;
    
    // Check if we have a valid time format (MM:SS)
    if (initialTime === "--:--") {
        // No countdown needed, we're not in school hours
        return;
    }
    
    // Parse the initial minutes and seconds
    const timeParts = initialTime.split(':');
    if (timeParts.length !== 2) {
        return; // Invalid format
    }
    
    let minutes = parseInt(timeParts[0], 10);
    let seconds = parseInt(timeParts[1], 10);
    
    // Total seconds for countdown
    let totalSeconds = minutes * 60 + seconds;
    
    // Update every second
    const countdownInterval = setInterval(function() {
        totalSeconds--;
        
        if (totalSeconds <= 0) {
            // Time's up, reload the page to get the next period
            clearInterval(countdownInterval);
            location.reload();
            return;
        }
        
        // Calculate minutes and seconds
        minutes = Math.floor(totalSeconds / 60);
        seconds = totalSeconds % 60;
        
        // Update the display
        timerDisplay.textContent = `${minutes.toString().padStart(2, '0')}:${seconds.toString().padStart(2, '0')}`;
        
        // Refresh the page every 5 minutes to ensure data stays current
        if (totalSeconds % 300 === 0) {
            location.reload();
        }
    }, 1000);
    
    // Settings functionality
    const settingsButton = document.getElementById('settingsButton');
    const settingsModal = document.getElementById('settingsModal');
    const closeSettings = document.getElementById('closeSettings');
    const themeToggle = document.getElementById('themeToggle');
    const saveSettings = document.getElementById('saveSettings');
    const classSettings = document.getElementById('classSettings');
    
    // Load settings from localStorage
    loadSettings();
    
    // Populate class settings
    populateClassSettings();
    
    // Open settings modal
    settingsButton.addEventListener('click', function() {
        settingsModal.classList.add('show');
    });
    
    // Close settings modal
    closeSettings.addEventListener('click', function() {
        settingsModal.classList.remove('show');
    });
    
    // Close modal when clicking outside
    settingsModal.addEventListener('click', function(e) {
        if (e.target === settingsModal) {
            settingsModal.classList.remove('show');
        }
    });
    
    // Toggle theme
    themeToggle.addEventListener('change', function() {
        document.documentElement.setAttribute('data-theme', this.checked ? 'dark' : 'light');
    });
    
    // Save settings
    saveSettings.addEventListener('click', function() {
        saveUserSettings();
        settingsModal.classList.remove('show');
        
        // Update class names without reloading
        updateClassNames();
    });
    
    // Function to convert temperature display
    function convertTemperatureDisplay() {
        const weatherInfo = document.querySelector('.weather-info');
        if (!weatherInfo) return;
        
        const tempUnit = localStorage.getItem('tempUnit') || 'F';
        const weatherText = weatherInfo.textContent;
        
        // Regex to extract temperature number and unit
        const tempRegex = /(-?\d+\.?\d*)°([FC])/;
        const match = weatherText.match(tempRegex);
        
        if (match) {
            const temp = parseFloat(match[1]);
            const currentUnit = match[2];
            
            // Only convert if current unit doesn't match desired unit
            if (currentUnit !== tempUnit) {
                let newTemp;
                if (tempUnit === 'C' && currentUnit === 'F') {
                    // F to C conversion
                    newTemp = ((temp - 32) * 5/9).toFixed(1);
                } else if (tempUnit === 'F' && currentUnit === 'C') {
                    // C to F conversion
                    newTemp = ((temp * 9/5) + 32).toFixed(1);
                } else {
                    return; // No conversion needed
                }
                
                // Replace the temperature in the text
                weatherInfo.textContent = weatherText.replace(
                    `${temp}°${currentUnit}`, 
                    `${newTemp}°${tempUnit}`
                );
            }
        }
    }
    
    // Function to load settings from localStorage
    function loadSettings() {
        // Load theme setting
        const theme = localStorage.getItem('theme') || 'light';
        document.documentElement.setAttribute('data-theme', theme);
        themeToggle.checked = theme === 'dark';
        
        // Load temperature unit setting
        const tempUnit = localStorage.getItem('tempUnit') || 'F';
        document.getElementById('unitF').checked = tempUnit === 'F';
        document.getElementById('unitC').checked = tempUnit === 'C';
        
        // Load class name customizations and apply them
        updateClassNames();
        
        // Convert temperature on page load
        convertTemperatureDisplay();
    }
    
    // Function to populate class settings
    function populateClassSettings() {
        // Clear existing content
        classSettings.innerHTML = '';
        
        // Get all unique period names
        const periodElements = document.querySelectorAll('[data-period-name]');
        const periodNames = new Set();
        
        periodElements.forEach(element => {
            const periodName = element.getAttribute('data-period-name');
            periodNames.add(periodName);
        });
        
        // Create input fields for each period
        periodNames.forEach(periodName => {
            // Skip if period name is empty or undefined
            if (!periodName) return;
            
            const savedName = localStorage.getItem(`class_${periodName}`) || '';
            
            const inputDiv = document.createElement('div');
            inputDiv.className = 'class-input';
            
            const label = document.createElement('label');
            label.textContent = periodName + ':';
            
            const input = document.createElement('input');
            input.type = 'text';
            input.placeholder = `Enter name for ${periodName}`;
            input.value = savedName;
            input.dataset.periodName = periodName;
            
            inputDiv.appendChild(label);
            inputDiv.appendChild(input);
            classSettings.appendChild(inputDiv);
        });
    }
    
    // Function to save user settings
    function saveUserSettings() {
        // Save theme setting
        localStorage.setItem('theme', themeToggle.checked ? 'dark' : 'light');
        
        // Save temperature unit setting
        const tempUnit = document.querySelector('input[name="tempUnit"]:checked').value;
        localStorage.setItem('tempUnit', tempUnit);
        
        // Save class name customizations
        const classInputs = document.querySelectorAll('.class-input input');
        classInputs.forEach(input => {
            const periodName = input.dataset.periodName;
            const customName = input.value.trim();
            
            if (customName) {
                localStorage.setItem(`class_${periodName}`, customName);
            } else {
                localStorage.removeItem(`class_${periodName}`);
            }
        });
        
        // Convert temperature display if needed
        convertTemperatureDisplay();
    }
    
    // Function to update class names in the UI
    function updateClassNames() {
        const periodElements = document.querySelectorAll('[data-period-name]');
        
        periodElements.forEach(element => {
            const periodName = element.getAttribute('data-period-name');
            const customName = localStorage.getItem(`class_${periodName}`);
            
            const nameSpan = element.querySelector('.custom-class-name');
            if (nameSpan && customName) {
                nameSpan.textContent = customName;
            }
        });
    }
});
