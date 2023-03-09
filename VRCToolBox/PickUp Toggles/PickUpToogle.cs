using UdonSharp;
using UnityEngine;
using VRC.SDKBase;
using VRC.Udon;

public class PickupsToggle : UdonSharpBehaviour
{
    public bool enablePickups = true;

    private void Start()
    {
        // Register the toggle function with the quick menu
        var menu = transform.GetComponent<QuickMenu>();
        menu.AddToggleButton("Pickups", () => { TogglePickups(); }, () => enablePickups, null);
    }

    public void TogglePickups()
    {
        // Find all VRC_Pickup objects in the scene
        var pickups = FindObjectsOfType<VRC_Pickup>();

        // Toggle each pickup object based on the value of enablePickups
        foreach (var pickup in pickups)
        {
            pickup.gameObject.SetActive(enablePickups);
        }

        // Update the value of enablePickups
        enablePickups = !enablePickups;
    }
}
