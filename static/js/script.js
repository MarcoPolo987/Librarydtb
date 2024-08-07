function toggleDropdown() {
    const dropdown = document.querySelector('.dropdown-content');
    const overlay = document.querySelector('.overlay');
  
    // Check transform property to determine dropdown's visibility
    if (window.getComputedStyle(dropdown).transform === "none" || window.getComputedStyle(dropdown).transform === "matrix(1, 0, 0, 1, 0, 0)") { // Matrix representation of translateX(0%)
        dropdown.style.transform = 'translateX(100%)';
        setTimeout(() => overlay.style.opacity = '0', 100);
        setTimeout(() => {
            overlay.style.display = 'none';
        }, 300); // Hide overlay after the slide and fade out
    } else {
        dropdown.style.transform = 'translateX(0%)'; // Slide the dropdown in
        overlay.style.display = 'block';
        setTimeout(() => overlay.style.opacity = '1', 100);
    }
  }
  