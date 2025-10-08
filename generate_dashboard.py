import matplotlib.pyplot as plt
import seaborn as sns
from sklearn.metrics import confusion_matrix, accuracy_score, precision_score, recall_score, f1_score
import os
y_true = [0, 1, 2, 0, 1, 2, 1, 0, 2, 2]
y_pred = [0, 0, 2, 0, 1, 2, 1, 0, 1, 2]

acc = accuracy_score(y_true, y_pred)
prec = precision_score(y_true, y_pred, average='weighted', zero_division=0)
rec = recall_score(y_true, y_pred, average='weighted', zero_division=0)
f1 = f1_score(y_true, y_pred, average='weighted', zero_division=0)

cm = confusion_matrix(y_true, y_pred)
labels = ['Low', 'Medium', 'High']  

# Plot
fig, axes = plt.subplots(1, 2, figsize=(14, 6))
metrics = {'Accuracy': acc, 'Precision': prec, 'Recall': rec, 'F1 Score': f1}
sns.barplot(x=list(metrics.keys()), y=list(metrics.values()), ax=axes[0], palette='Set2')
axes[0].set_title('Model Performance Metrics')
axes[0].set_ylim(0, 1.05)
axes[0].grid(axis='y', linestyle='--', alpha=0.7)
for i, v in enumerate(metrics.values()):
    axes[0].text(i, v + 0.02, f"{v:.2f}", ha='center')

sns.heatmap(cm, annot=True, fmt='d', cmap='Blues',
            xticklabels=labels, yticklabels=labels, cbar=False, ax=axes[1])
axes[1].set_title('Confusion Matrix')
axes[1].set_xlabel('Predicted')
axes[1].set_ylabel('Actual')

plt.tight_layout()


output_path = os.path.join("static", "dashboard.png")
plt.savefig(output_path)
plt.close()
