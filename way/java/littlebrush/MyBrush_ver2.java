package brush;

import brush.MyBrush_ver1;

import javax.swing.*;
import java.awt.*;
import java.awt.event.ActionEvent;
import java.awt.event.ActionListener;
import java.awt.Graphics;

public class MyBrush_ver2 extends JFrame implements MouseListener {

    public MyBrush_ver2() {
        super("My little tiny brush, on the way to...");
        JPanel cp = new JPanel(new BorderLayout());
        cp.setBorder(BorderFactory.createCompoundBorder(BorderFactory.createEmptyBorder(5, 5, 5, 5),
            BorderFactory.createLineBorder(Color.black)));
        setContentPane(cp);
        cp.add(new MyBrush_ver1(), BorderLayout.CENTER);
        JButton btn = new JButton("Close");
        btn.addActionListener(new ActionListener(){
            public void actionPerformed(ActionEvent e) {
                System.exit(0);
            }
        });
        cp.add(btn, BorderLayout.SOUTH);
        cp.setBackground(Color.green);
        setSize(500, 400);
        setLocationRelativeTo(null);
        setDefaultCloseOperation(EXIT_ON_CLOSE);

        Graphics g = cnvs.getGraphics();
        g.setColor(new)
    }

    public static void main(String[] args) {
        new MyBrush_ver2().setVisible(true);
    }
}