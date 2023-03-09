using UdonSharp;
using UnityEngine;
using VRC.SDKBase;
using VRC.Udon;

public class MirrorToggle : UdonSharpBehaviour
{
    public GameObject mirrorObject;

    private void Start()
    {
        // Check if a mirror object has been assigned
        if (mirrorObject == null)
        {
            Debug.LogError("MirrorToggle: No mirror object assigned.");
            return;
        }

        // Get the mirror component from the mirror object
        var mirror = mirrorObject.GetComponentInChildren<VRC_Mirror>();

        // Check if a mirror component was found
        if (mirror == null)
        {
            Debug.LogError("MirrorToggle: No mirror component found.");
            return;
        }

        // Register the toggle function with the quick menu
        var menu = transform.GetComponent<QuickMenu>();
        menu.AddToggleButton("Mirror", () => { ToggleMirror(mirror); }, () => mirror.isActiveAndEnabled, null);
    }

    public void ToggleMirror(VRC_Mirror mirror)
    {
        mirror.enabled = !mirror.enabled;
    }
}
