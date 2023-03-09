using UdonSharp;
using UnityEngine;
using UnityEngine.UI;
using VRC.SDKBase;
using VRC.Udon;

public class MenuTools : UdonSharpBehaviour
{
    public Toggle flyingToggle;

    public void Start()
    {
        var menu = transform.Find("UserInterface/QuickMenu/QuickMenu_NewElements/_InfoBar/InfoBar").GetComponent<QuickMenu>();
        var toolsButton = menu.transform.Find("ShortcutMenu/ToolsButton");

        // Check if the Tools button already exists
        if (toolsButton == null)
        {
            // Create the Tools button
            var button = Instantiate(menu.transform.Find("ShortcutMenu/_HelpButton").gameObject, menu.transform.Find("ShortcutMenu"));
            button.name = "ToolsButton";
            button.transform.Find("Text").GetComponent<Text>().text = "Tools";
            button.transform.Find("Icon").GetComponent<Image>().sprite = Resources.Load<Sprite>("icon_unityeditor");

            // Create the submenu for the Tools button
            var subMenu = Instantiate(menu.transform.Find("UserInteractMenu/ForceLogoutButton").gameObject, menu.transform);
            subMenu.name = "ToolsSubMenu";
            subMenu.transform.localPosition = new Vector3(0, -75, 0);
            subMenu.transform.Find("LogoutButton").gameObject.SetActive(false);
            subMenu.transform.Find("ReturnButton").gameObject.SetActive(false);

            // Add the flying toggle button to the Tools submenu
            var flyingButton = Instantiate(menu.transform.Find("UserInteractMenu/Public/Udon/UdonMenuSystem/Button_Prefabs/Toggle").gameObject, subMenu.transform);
            flyingButton.name = "FlyingToggle";
            flyingButton.transform.localPosition = new Vector3(0, -25, 0);
            flyingButton.transform.Find("Text").GetComponent<Text>().text = "Flying";
            flyingButton.GetComponentInChildren<Toggle>().onValueChanged.AddListener(SetFlying);

            // Add the Tools button to the main menu
            menu.AddButton("Tools", () => { subMenu.SetActive(true); }, null, QuickMenu.UserIcon.None);
        }
    }

    public void SetFlying(bool value)
    {
        if (Networking.LocalPlayer != null)
        {
            var playerController = Networking.LocalPlayer.GetComponent<VRCPlayerApi>();
            playerController.SetFlyMode(value);
        }
    }
}
