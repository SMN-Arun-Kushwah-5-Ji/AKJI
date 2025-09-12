import javax.swing.*;
import java.awt.*;
import java.io.*;

public class ADBManager extends JFrame {
    private JTextArea output;
    private JTextField ipField;
    private JLabel status;

    public ADBManager() {
        setTitle("Advanced ADB Wireless Control");
        setSize(700, 400);
        setDefaultCloseOperation(EXIT_ON_CLOSE);

        JPanel panel = new JPanel(new BorderLayout());

        // Top
        JPanel top = new JPanel();
        top.add(new JLabel("Enter Mobile IP:"));
        ipField = new JTextField(15);
        top.add(ipField);
        status = new JLabel("Not connected");
        status.setForeground(Color.RED);
        top.add(status);

        panel.add(top, BorderLayout.NORTH);

        // Center
        output = new JTextArea();
        output.setEditable(false);
        JScrollPane scroll = new JScrollPane(output);
        panel.add(scroll, BorderLayout.CENTER);

        // Buttons
        JPanel btnPanel = new JPanel(new GridLayout(2, 4, 5, 5));
        addButton(btnPanel, "Connect", () -> runADB("connect " + ipField.getText() + ":5555"));
        addButton(btnPanel, "Disconnect", () -> runADB("disconnect"));
        addButton(btnPanel, "Reboot", () -> runADB("reboot"));
        addButton(btnPanel, "List Devices", () -> runADB("devices"));
        addButton(btnPanel, "Push File", () -> runADB("push test.txt /sdcard/Download/"));
        addButton(btnPanel, "Pull File", () -> runADB("pull /sdcard/Download/test.txt ./"));
        addButton(btnPanel, "Custom", () -> {
            String cmd = JOptionPane.showInputDialog(this, "Enter adb command (without 'adb'):");
            if (cmd != null) runADB(cmd);
        });
        addButton(btnPanel, "Clear Output", () -> output.setText(""));

        panel.add(btnPanel, BorderLayout.SOUTH);

        add(panel);
    }

    private void addButton(JPanel panel, String name, Runnable action) {
        JButton btn = new JButton(name);
        btn.addActionListener(e -> action.run());
        panel.add(btn);
    }

    private void runADB(String cmd) {
        try {
            Process process = new ProcessBuilder("adb", cmd.split(" ")).start();
            BufferedReader reader = new BufferedReader(new InputStreamReader(process.getInputStream()));
            String line;
            while ((line = reader.readLine()) != null) {
                output.append(line + "\n");
            }
            process.waitFor();
        } catch (Exception e) {
            output.append("Error: " + e.getMessage() + "\n");
        }
    }

    public static void main(String[] args) {
        SwingUtilities.invokeLater(() -> new ADBManager().setVisible(true));
    }
}
