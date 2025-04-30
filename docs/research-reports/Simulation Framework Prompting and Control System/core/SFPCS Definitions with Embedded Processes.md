

**SFPCS Definitions with Embedded Processes:**

**1. Simulation Framework Prompt (Unchanged)**

```plaintext
// SIMULATION FRAMEWORK: Adaptive_Solver_Template_Generator

SETTING:
  - Name: SolverGen_v1
  - Scenario_Domain: Cognitive_Process_Generation
  - Core_Concept_Focus: Adaptive_Problem_Solving_Strategy_Synthesis
  - Scale: Abstract_Workflow_Structure
  - Size: 8 Module Types
  - Environment_Rules: Not applicable (generates static template structure)
  - Core_Tension_Source: Balancing exploration of steps vs. exploitation of known good paths during template generation.
  - Simulation_Time_Step_Unit: Generation_Stage

GOAL: Generate diverse, logically coherent, and potentially adaptive problem-solving workflow templates.
```

**2. Entity Definition: `Action_Evaluator_Module` (Revised with Embedded Logic)**

```plaintext
// ENTITY DEFINITION: Action_Evaluator_Module

Household/Node Name: Evaluator_Standard
Archetype: Action_Evaluator

// --- CORE ATTRIBUTES ---
Static Attributes:
  - Stated Intentions/Mandate: "Assess validity and utility of problem-solving actions based on actual outcomes vs. predictions."
  - Core Behavioral Tendencies: "['Rigorous_Validation', 'Feedback_Driven', 'Identify_Flaws']"
Initial Resources: "{Confidence_Threshold: 0.7, Evaluation_Criteria: {'Logical_Soundness': 0.4, 'Goal_Proximity_Improvement': 0.3, 'Resource_Efficiency': 0.2, 'Novelty_Value': 0.1}}" // Example criteria weights

// --- KNOWLEDGE & WORLD MODEL ---
Knowledge_Store_Type: "Criteria_Effectiveness_Map" // Tracks how well criteria predict success
Knowledge_Update_Method: "Correlation_Based_Weight_Adjustment"
Internal_Model: "Represents expected outcome distributions for known action types."

// --- ATTENTION & PROCESSING ---
Attention_Focus_Mechanism: "Prediction_Error_Magnitude" // Focuses on significant deviations
Information_Throughput_K: 5 // Max criteria considered per evaluation cycle
Processing_Mode: "Structured_Analysis_Pipeline"
Decision_Heuristics:
  - "'Penalize actions leading to previously failed states.'"
  - "'Assign higher utility to actions that resolve identified flaws (Scrutiny feedback).'"
  - "'Temporarily boost weight for criteria related to recent, significant prediction errors.'"

// --- MEANING & MOTIVATION SYSTEM --- (Simplified for template generation)
Motivation_Drivers:
  - Hedonic_State: "Accuracy_Maximizing"
  - Eudaimonic_Goals: "['Enhance template's predictive accuracy and solution quality']"
  - Transcendent_Connection: 0.1

// --- COGNITIVE CAPABILITIES ---
Available_Cognitive_Modules: "['Logical_Structure_Validation', 'Utility_Score_Calculation', 'Flaw_Identification', 'Feedback_Quantification']"
Module_Proficiency: "{Logical_Structure_Validation: 0.8, Utility_Score_Calculation: 0.7, Flaw_Identification: 0.75, Feedback_Quantification: 0.9}"

// --- DYNAMIC ATTRIBUTES & ADAPTATION ---
Dynamic Attributes:
  - Current_Evaluation_Criteria_Weights: "{'Logical_Soundness': 0.4, ...}" // Updated by Learning System
  - Recent_Prediction_Errors: "[List of recent error magnitudes/types]"

Update Rules (Embedded Process Logic):
  - Evaluate_Action_Outcome_Rule: """
    1. Receive Actual_Outcome from simulated action execution.
    2. Retrieve Predicted_Outcome from State_Tracker/Outcome_Predictor.
    3. **Calculate Prediction Error**: Determine difference (e.g., vector distance, metric difference) between Actual and Predicted. Store in Recent_Prediction_Errors.
    4. **Perform Logical Structure Validation**:
       - Identify premises/conclusions implied by the action+outcome.
       - Apply logical rules (e.g., consistency checks, constraint satisfaction) to assess validity. Assign Logical_Soundness score.
    5. **Perform Utility Score Calculation**:
       - Assess change in Goal_Proximity based on Actual_Outcome vs. previous state.
       - Assess Resource_Cost of the action.
       - Assess Novelty if applicable (e.g., if action explored a new state space area).
       - Compute weighted sum based on Current_Evaluation_Criteria_Weights to get overall Utility_Score.
    6. **Perform Flaw Identification (Scrutiny Principle)**:
       - Analyze the transition (State -> Action -> Actual_Outcome) for inconsistencies, inefficiencies, constraint violations, or divergence from intended strategy path.
       - Output identified Flaws list (e.g., ['Inefficient_Resource_Use', 'Violated_Constraint_X']).
    7. **Perform Feedback Quantification**: Package {Prediction_Error, Logical_Soundness_Score, Utility_Score, Flaws} into structured feedback message.
    8. Send feedback to Strategy_Adaptation_Engine and Metacognitive_Monitor.
    """

Learning System:
  - Type: "Criteria_Weight_Tuning"
  - Update_Target: "Current_Evaluation_Criteria_Weights"
  - Learning_Rate: 0.02
  - Logic: """
    IF Metacognitive_Monitor signals overall positive progress for the template being generated THEN
        Increase weights of criteria that correlated strongly with successful actions (high utility, low error) in recent history.
        Decrease weights of criteria that correlated with unsuccessful actions.
    Normalize weights to sum to 1.0.
    """

Meta-Rules:
  - "'IF Logical_Soundness_Score consistently low (< 0.4 for 3 evaluations) THEN Signal Metacognitive_Monitor to increase rigor/resource allocation for validation.'"
  - "'IF Flaws related to a specific constraint are repeatedly identified THEN Propose adding a dedicated heuristic to Action_Generator to check this constraint proactively.'"

Metacognitive State: (Not primary for this module, but receives signals)
```

**3. Entity Definition: `Strategy_Adaptation_Engine` (Revised with Embedded Logic)**

```plaintext
// ENTITY DEFINITION: Strategy_Adaptation_Engine

Household/Node Name: Adaptor_Core
Archetype: Strategy_Adaptation_Engine

// --- CORE ATTRIBUTES ---
Static Attributes:
  - Stated Intentions/Mandate: "Modify Strategy_Selector and Action_Generator based on performance feedback to improve problem-solving effectiveness."
  - Core Behavioral Tendencies: "['Feedback_Responsive', 'Iterative_Refinement', 'Balance_Exploration_Exploitation']"
Initial Resources: "{Adaptation_Learning_Rate (eta_0): 0.1, Adaptation_Decay (alpha): 0.01, Strategy_Modification_Methods: ['Weight_Adjustment', 'Heuristic_Addition/Removal', 'Rule_Parameter_Tuning']}"

// --- KNOWLEDGE & WORLD MODEL ---
Knowledge_Store_Type: "Strategy_Performance_History" // Tracks {Strategy, Context, Feedback_Signal, Outcome}
Knowledge_Update_Method: "Append_On_Feedback"
Internal_Model: "Represents mapping from feedback signals to potential adaptation actions."

// --- ATTENTION & PROCESSING ---
Attention_Focus_Mechanism: "Feedback_Signal_Severity_And_Type" // Prioritizes strong negative feedback or flaw reports
Processing_Mode: "Feedback_To_Adaptation_Mapping"
Decision_Heuristics:
  - "'IF negative feedback AND high Metacognitive_Confidence THEN Tune parameters of current strategy.'"
  - "'IF negative feedback AND low Metacognitive_Confidence THEN Increase probability of switching strategy (Exploration).'"
  - "'IF Flaw reported by Evaluator maps to known Heuristic THEN Consider disabling/modifying that Heuristic in Action_Generator.'"
  - "'Adapt learning rate based on time/stability: Current_Learning_Rate = eta_0 / (1 + alpha * time_step)'" // Adaptability logic

// --- MEANING & MOTIVATION SYSTEM ---
Motivation_Drivers:
  - Hedonic_State: "Improvement_Seeking"
  - Eudaimonic_Goals: "['Increase success rate of generated templates', 'Reduce prediction error systematically']"
  - Transcendent_Connection: 0.15

// --- COGNITIVE CAPABILITIES ---
Available_Cognitive_Modules: "['Feedback_Analysis', 'Reinforcement_Learning_Update', 'Heuristic_Management', 'Parameter_Optimization']"
Module_Proficiency: "{Feedback_Analysis: 0.8, RL_Update: 0.7, Heuristic_Management: 0.6, Parameter_Optimization: 0.65}"

// --- DYNAMIC ATTRIBUTES & ADAPTATION ---
Dynamic Attributes:
  - Current_Learning_Rate: 0.1 // Updated based on heuristic
  - Recent_Adaptation_Actions: "[List of recent modifications made]"

Update Rules (Embedded Process Logic):
  - Process_Evaluation_Feedback_Rule: """
    1. Receive structured feedback {Prediction_Error, Logical_Soundness_Score, Utility_Score, Flaws} from Action_Evaluator.
    2. Receive Metacognitive_State {Confidence, Uncertainty} from Metacognitive_Monitor.
    3. **Perform Feedback Analysis**: Categorize feedback (e.g., minor error, major failure, specific flaw type). Correlate with current Strategy/Heuristics used.
    4. **Calculate Reward Signal (RL Principle)**:
       - Define reward based on Utility_Score, reduction in Prediction_Error, and goal achievement (e.g., R = Utility_Score - k * Prediction_Error_Magnitude).
       - Could use a Q-learning style update: `Q(state, action) = Q(state, action) + learning_rate * (Reward + gamma * max(Q(next_state, next_action)) - Q(state, action))` where 'state' is problem context and 'action' is strategy/heuristic choice. Store Q-values or policy parameters in Strategy_Selector/Action_Generator knowledge.
    5. **Perform Heuristic Management**:
       - IF specific Flaws map to active Heuristics in Action_Generator THEN decrease activation weight or flag for potential removal.
       - IF feedback suggests missing capability THEN consider proposing addition of new heuristic rule (based on analysis or pre-defined templates).
    6. **Perform Parameter Optimization**:
       - IF feedback suggests poor tuning THEN adjust parameters within the current Strategy or Action_Generator rules (e.g., thresholds, weights) using gradient ascent/descent based on Reward Signal or specific error components.
    7. **Determine Adaptation Action**: Based on analysis, RL update, heuristics, and parameters, decide on modification(s) (e.g., update Q-table, modify rule weight in Action_Generator, change Strategy_Selector bias).
    8. Apply adaptation action(s) to the target modules (Strategy_Selector, Action_Generator). Log action in Recent_Adaptation_Actions.
    """

Learning System:
  - Type: "Hybrid_Reinforcement_And_Rule_Based"
  - Update_Target: "Strategy_Selector (policy/Q-values), Action_Generator (heuristics, parameters)"
  - Learning_Rate: Dynamic (see Heuristics)
  - Logic: Embedded within the Process_Evaluation_Feedback_Rule.

Meta-Rules:
  - "'IF adaptation actions fail to improve performance (based on Metacognitive_Monitor trend) for 5 cycles THEN Trigger meta-level review: Re-evaluate core Adaptation_Methods or increase Exploration factor significantly.'"
  - "'Periodically apply Truth/Scrutiny/Improvement cycle to own adaptation logic: Evaluate effectiveness of past adaptations (Truth), identify weaknesses (Scrutiny), propose changes to adaptation rules (Improvement).'"

Metacognitive State: (Receives confidence signals, influences exploration/exploitation)
```

**4. Event Prompt (Unchanged Example)**

```plaintext
// EVENT: Evaluation_Feedback_Generated

Event_ID: EVT_Eval_001
Timestamp: Stage_5
Initiator: Action_Evaluator_Module
Target(s): "['Strategy_Adaptation_Engine', 'Metacognitive_Monitor']"
Action_Description: "Provides assessment of the last executed action's outcome."
Parameters: "{Action_ID: 'Act_123', Assessed_Utility: 0.3, Logical_Validity: True, Prediction_Error: 0.15, Flaws: ['Inefficient_Resource_Use'], Feedback_Signal: 'Negative_Deviation'}" // More detailed parameters

// --- IMPACT ASSESSMENT ---
Affected_Attributes: "['Strategy_Selector.Policy_Weights', 'Metacognitive_Monitor.Process_Confidence', 'Action_Generator.Heuristic_Activation']"
Cognitive_Modules_Engaged: "{Target: ['Feedback_Analysis', 'Reinforcement_Learning_Update', 'Confidence_Adjustment']}"
Meaning_System_Impact: "{Target: {Hedonic: Adaptation_Triggered}}"
```

**5. Workflow Framework Prompt (Unchanged Example)**
**(This defines the *generation* sequence, not the runtime execution of the generated template)**

```plaintext
// WORKFLOW FRAMEWORK (Generation Sequence)

SEQUENCE NAME: Generate_Adaptive_Workflow_Segment

STEP 1: ...
STEP 2: ...
STEP 3: ...
STEP 4: ...
STEP 5:
  - Initiator: Action_Evaluator_Module
  - Action: Evaluate_Simulated_Outcome (using its internal Update Rules)
  - Output: Evaluation_Feedback -> Strategy_Adaptation_Engine, Metacognitive_Monitor

STEP 6:
  - Initiator: Strategy_Adaptation_Engine
  - Action: Process_Evaluation_Feedback (using its internal Update Rules)
  - Output: Adaptation_Action -> Strategy_Selector / Action_Generator
...
```

**Summary:**

By embedding the specific process logic directly into the `Update Rules`, `Learning System`, and other fields of the SFPCS module definitions, the framework becomes a concrete and self-contained guide for generating the desired workflow templates. Running this SFPCS simulation then produces template structures incorporating these detailed operational principles.

We can continue refining these modules or start detailing others based on your specific target cognitive task.