using UnityEngine;
using System.Collections;
using System.Collections.Generic;

public class DynamicBoneCreator : MonoBehaviour {

    public GameObject targetObject;
    public List<Transform> bonesToAttach;
    public float damping = 0.2f;
    public float elasticity = 0.05f;
    public float stiffness = 0.8f;
    public float inert = 0f;

    void Start () {
        DynamicBone[] dynamicBones = targetObject.GetComponents<DynamicBone>();
        if (dynamicBones == null || dynamicBones.Length == 0) {
            DynamicBone dynamicBone = targetObject.AddComponent<DynamicBone>();
            dynamicBone.m_Root = targetObject.transform;
            dynamicBone.m_Damping = damping;
            dynamicBone.m_Elasticity = elasticity;
            dynamicBone.m_Stiffness = stiffness;
            dynamicBone.m_Inert = inert;
            dynamicBone.m_UpdateRate = DynamicBone.UpdateRate.LateUpdate;

            dynamicBone.m_EndLength = 0.1f;
            dynamicBone.m_Gravity = new Vector3(0f, -0.1f, 0f);
            dynamicBone.m_Force = new Vector3(0f, 0f, 0f);
            dynamicBone.m_Colliders = new List<DynamicBoneColliderBase>();
            dynamicBone.m_Exclusions = new List<Transform>();
            dynamicBone.m_FreezeAxis = DynamicBone.FreezeAxis.None;
            dynamicBone.m_DistantDisable = false;
            dynamicBone.m_DistanceToObject = 0f;
            dynamicBone.m_ReferenceObject = null;
            dynamicBone.m_DistanceToObject = 0f;
        }

        for (int i = 0; i < bonesToAttach.Count; i++) {
            DynamicBoneCollider dynamicBoneCollider = bonesToAttach[i].gameObject.AddComponent<DynamicBoneCollider>();
            dynamicBoneCollider.m_Center = bonesToAttach[i];
            dynamicBoneCollider.m_Radius = 0.05f;
            dynamicBoneCollider.m_Height = 0.1f;
            dynamicBoneCollider.m_Direction = new Vector3(0f, 0f, 0f);
        }
    }
}
